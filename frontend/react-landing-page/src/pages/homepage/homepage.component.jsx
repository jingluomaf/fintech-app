import React from "react";

import Directory from "../../components/directory/directory.component";

import { HomePageContainer } from "./homepage.styles";

const HomePage = () => (
  <HomePageContainer>
    <Directory />
    <a href="http://localhost:8888">jupyter</a>
    <a href="http://localhost:8000">django</a>
    <a href="http://localhost:9000">minio</a>
    <a href="http://localhost:9090">portainer</a>
    <a href="http://localhost:8080">airflow</a>
  </HomePageContainer>
);

export default HomePage;
