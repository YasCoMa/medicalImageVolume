## Summary
This repository is a web application to handle medical images in dcm (dicom) format with the purpose of calculating the volume of image segments that have a higher contrast. This application contains the api with the function to receive the uploaded image and return the volume, and the front end web application that contains a form to drag and drop the image.

### Tech stack
- Backend: FastApi
- Frontend: Nuxt 3

### Configuring the backend api
- cd api-backend
- docker-compose up --build (in case there is no image yet)
- docker-compose up

### Testing the api
- docker exec -it api-backend_web_1 /bin/bash
- pytest

### Configuring the frontend web application
- cd webapp-frontend
- docker-compose up --build (in case there is no image yet)
- docker-compose up

### Access endpoints
- Backend: http://127.0.0.1:8000
- Frontend: http://127.0.0.1:3002

## Future work
This implementation only selects the regions of the image considering a single threshold value, it may lead to find false positives if health regions of the pixels have high intensity values. A better solution would involve applying convolution windows as filters and then apply the volume calculation.

