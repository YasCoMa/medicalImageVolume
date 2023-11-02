import pydicom
import numpy as np
from PIL import Image
from skimage import measure

class DicomProcessing:
    """
    Class to deal with the dicom medical images normalization, filtering and volume calculation
    """

    def extractPixelData(self, filename):
        """
        Read dicom image and extracts the array of pixels from the image.

        Parameters
        ----------
        filename : str, mandatory
            The name or binary data of the image file

        Returns
        ------
        img : Pydicom FileDataset
            Dicom image object with all the metadata
        pixelData : Numpy Array
            2D Array with the raw gray scale pixel data ranging from 0 to 255
            
        Reference: https://github.com/tueimage/essential-skills/blob/master/pydicom.md
        """
        
        img = pydicom.dcmread(filename, force=True)
        pixelData = img.pixel_array
        
        return img, pixelData

    def normalize(self, pixelData):
        """
        Normalize the array with color values in a range of 0 to 1

        Parameters
        ----------
        pixelData : Numpy Array, mandatory
            2D Array with the raw gray scale pixel data ranging from 0 to 255

        Returns
        ------
        normalizedData : Numpy Array
            2D Array with the normalized pixel data ranging from 0 to 1
        """
        
        normalizedData = ( pixelData - np.min(pixelData) ) / ( np.max(pixelData) - np.min(pixelData) ) 
        
        return normalizedData
        
    def thresholdFilter(self, normalizedData, threshold=0.5):
        """
        Filter array of pixels highlighting the locations that are above a certain threshold

        Parameters
        ----------
        normalizedData : Numpy Array, mandatory
            2D Array with the normalized pixel data ranging from 0 to 1
        threshold : float, optional
            Threshold value to get the highlighted regions of the image (default is 0.5)

        Returns
        ------
        filteredData : Numpy Array
            2D Array with the filtered array of pixels contrasting the pixel locations above the threshold
        pixelsAboveCutoff : int
            Number of pixels above the given threshold
        """
        
        originalShape = normalizedData.shape
        tempData = normalizedData.flatten()
        pixelsAboveCutoff = len(np.where( tempData > threshold )[0])
        filteredData = np.where( tempData <= threshold, 0, 1)
        filteredData = np.reshape(filteredData, originalShape )
        
        return filteredData, pixelsAboveCutoff
        
    def calculateVolume(self, dcImg, filteredData):
        """
        Filter array of pixels highlighting the locations that are above a certain threshold

        Parameters
        ----------
        dcImg : Pydicom FileDataset, mandatory
            Dicom image object with all the metadata
        filteredData : Numpy Array, mandatory
            2D Array with the filtered array of pixels contrasting the pixel locations above the threshold

        Returns
        ------
        volume : float
            Volume value
        
        Reference: https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_regionprops.html
        """
        
        h = float( dcImg[0x00180050].value ) # Extracting the slice thickness property of the original medical image corresponding to the third component to be used in the volume calculation
        
        # Calculating volume by identifying specific regions
        labels = measure.label(filteredData) # Getting label of the regions found, it is using the default connectivity value (number of dimensions of filteredData)
        
        properties = measure.regionprops(labels, filteredData) # Calculate the properties of all the labeled regions including the area
        
        volume = sum( list( map( lambda p: h*p.area, properties) ) )  # Calculate volume using the sum of the product between all region areas and the height of the slice
        
        """
        More direct alternative:
        
        table = measure.regionprops_table(mat, properties=['area'] ) # Without the need of label identification
        volume = table['area'][0] * h
        """
        
        return volume
        
    def runVolumePipeline(self, fileName, threshold=0.5 ):
        """
        Filter array of pixels highlighting the locations that are above a certain threshold

        Parameters
        ----------
        filename : str, mandatory
            The name of the image file
        threshold : float, optional
            Threshold value to get the highlighted regions of the image (default is 0.5)

        Returns
        ------
        volume : float
            Volume value
        """
        
        img, pixelData = self.extractPixelData(fileName)
        normData = self.normalize(pixelData)
        filteredData, pixelsAboveCutoff = self.thresholdFilter(normData, threshold)
        volume = self.calculateVolume(img, filteredData)
        
        return pixelsAboveCutoff, volume
        
    def renderImage(self, processedImageData):
        img = Image.fromarray(np.uint8(processedImageData * 255) , 'L')
        img.save('data/processedImage.png')
        

