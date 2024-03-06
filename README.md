<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Category-App][app-shield]][app-url]





<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Gozzi98/merchant_ai">
    
<h3 align="center">Product Category Generator</h3>

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
A friend of mine works for an e-commerce company that offers a marketplace to vendors. The challenge is being able to automate extraction of standardized product categories from ambiguous product description data. By leveraging ChatGPT to develop a program that automates the categorization process, making it simpler to manipulate and manage product data.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![PYTHON][Python.py]][Python-url]
* [![JSON][Json.json]][Json-url]
* [![OPENAI][Openai.ai]][Openai-url]
* [![OS][Os.os]][Os-url]
* [![FastAPi][Fast.api]][Fastapi-url]
* [![BaseModel][Base.model]][BaseModel-url]
  


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Need a Google Cloud account, access to gcloud CLI and Docker knowledge.

### Prerequisites

* Connect the gcloud CLI to GCP account
  ```sh
  gcloud auth login
  ```
* Set up your project ID
  ```sh
  gcloud config set project PROJECT_ID
  ```
* Region settings
  ```sh
  gcloud config set run/region REGION
  ```
* Docker settings
  ```sh
  gcloud auth configure-docker
  ```
* Prepare Dockerfile in the same hierarchy as the app directory.
  ```sh
  FROM python:3.11.3
  ENV PYTHONUNBUFFERED True
  
  RUN pip install --upgrade pip
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt

  ENV APP_HOME /root
  WORKDIR $APP_HOME
  COPY main.py $APP_HOME/category_app/

  EXPOSE 8080
  CMD ["uvicorn", "category_app.main:app", "--host", "0.0.0.0", "--port", "8080"]
  ```
* Now that it is ready, deploy to Cloud Run.
  ```sh
   gcloud run deploy category-app --port 8080 --source .
  ```
### Installation

1. Get a free API Key at [https://openai.com](https://openai.com)
2. Create .env file to store API key
   ```sh
   OPENAI_KEY= "API_KEY"
   ```
3. Using OPENAI.CHAT.COMPLETION to create a model response message to communicate with ChatGPT
   ```sh
   response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
   ```
4. Made different endpoints using POST and GET
   ```sh
   @app.get("/")
   (...)
   @app.post("/generate-product-category/")
   (...)
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tsemach David Gozlan 

Project Link: [https://github.com/Gozzi98/merchant_ai](https://github.com/Gozzi98/merchant_ai)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[app-shield]: https://img.shields.io/badge/-Category-App-black.svg?style=for-the-badge&logo=category-app&colorB=555
[app-url]: https://category-app-ierfjrurbq-ue.a.run.app
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/david-tsemach-gozlan/
[product-screenshot]: images/screenshot.png
[Python.py]: https://img.shields.io/badge/python-35495E?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Json.json]: https://img.shields.io/badge/json-DD0031?style=for-the-badge&logo=json&logoColor=white
[Json-url]: https://json.org/
[Openai.ai]: https://img.shields.io/badge/openai-FF2D20?style=for-the-badge&logo=openai&logoColor=4FC08D
[Openai-url]: https://openai.com/
[Os.os]: https://img.shields.io/badge/os-35495E?style=for-the-badge&logo=os&logoColor=white
[Os-url]: https://docs.python.org/3/library/os.html
[Fast.api]: https://img.shields.io/badge/fastapi-4A4A55?style=for-the-badge&logo=fastapi&logoColor=FF3E00
[Fastapi-url]: https://fastapi.tiangolo.com/
[Base.model]: https://img.shields.io/badge/basemodel-FF2D20?style=for-the-badge&logo=basemodel&logoColor=white
[BaseModel-url]: https://docs.pydantic.dev/latest/api/base_model/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
