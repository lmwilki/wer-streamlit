# Word Error Rate (WER) Streamlit App

This is a simple [Streamlit](https://www.streamlit.io/) app that calculates the Word Error Rate (WER) between two strings both in individual and bulk modes. All results can be exported in CSV and JSON formats.

## Installation

```bash
pip install -r requirements.txt
```

### DevContainer

If you are using [VSCode](https://code.visualstudio.com/) you can use the [DevContainer](https://code.visualstudio.com/docs/remote/containers) to run the app in a containerized environment. Just open the project in VSCode and click on the green button at the bottom left corner of the screen.

## Usage

### Locally

```bash
streamlit run app.py
```

### Containerised Web App

```bash
docker build -t wer-streamlit-app .
docker run -p 8501:8501 wer-streamlit-app
```

You can now access the app at http://localhost:8501

### How to download and export Docker image to zip file

```bash
docker save -o wer-streamlit-app.tar wer-streamlit-app
```

Can take a while to export the image. File is around 2GB.

### How to load Docker image from zip file

```bash
docker load -i wer-streamlit-app.tar
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.