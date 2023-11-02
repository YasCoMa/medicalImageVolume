export const useMedicalImage = () => {

  function calculateVolume(formData){
    const config = useRuntimeConfig();
    return useFetch( `${config.public.apiBase}calculate-dicom-image-volume`, {
        method: 'POST',
        body: formData
    });
  }

  return { calculateVolume };
};
