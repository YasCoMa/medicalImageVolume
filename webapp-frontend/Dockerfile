FROM node:18 AS development

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}

WORKDIR /usr/src/app

COPY ./webapp/package*.json ./

RUN npm install --legacy-peer-deps

COPY ./webapp .
COPY ./.env .

EXPOSE 3002
