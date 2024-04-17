# Coding Challenge MLE

## Einführung

Die vorgeschlagene Anwendung extrahiert informationsbezogene Stimmungsdaten aus Texten, konzentriert sich auf den Subtext und analysiert die Stimmung.

## Installation

- Klonen Sie dieses Repository:

    ```bash
    git clone https://github.com/NadiaSbaa/CodingChallenge_MLE.git
    ```

- Navigieren Sie zum Projektverzeichnis:

    ```bash
    cd CodingChallenge_MLE
    ```

### Erstellen und Ausführen

- Bauen Sie das Docker-Image:
     ```bash
    docker build -t sentiment_text_extractor .
    ```
    - **sentiment_text_extractor** ist nur ein Beispiel. Sie können einen anderen Namen wählen.


- Starten Sie den Docker-Container:
     ```bash
    docker run -p 8000:8000 sentiment_text_extractor .
    ```

### Endpunkte

- **GET /predict**: Vorhersage von Texten, die stimmungsbezogene Informationen aus dem bereitgestellten Text und der Stimmung ausdrücken.

    - **Anfrageparameter**:
        - `text` (string): Der Eingabetext für die Stimmungsanalyse.
        - `sentiment` (string): Der Stimmungstyp zur Analyse (`positiv`, `negativ` oder `neutral`).

    - **Beispielanfrage**:
        ```bash
        curl -X GET -H "Content-Type: application/json" -d '{"text": "Ich liebe dieses Produkt", "sentiment": "positiv"}' http://localhost:8000/predict
        ```

    - **Beispielantwort**:
        ```json
        {"selected_text": "liebe"}
        ```
    - **Fehlerbehandlung**:
        - Wenn der Parameter `text` fehlt oder leer ist:
            - Antwort: `400 Bad Request`
            - Fehlermeldung: `Missing / Empty parameter: text`

        - Wenn der Parameter `sentiment` fehlt oder leer ist:
            - Antwort: `400 Bad Request`
            - Fehlermeldung: `Missing / Empty parameter: sentiment`

        - Wenn der Wert des Parameters `sentiment` ungültig ist:
            - Antwort: `400 Bad Request`
            - Fehlermeldung: `Invalid sentiment value. Sentiment can be positive, negative or neutral`

### Testen

- Führen Sie innerhalb des Docker-Containers aus:
     ```bash
    docker exec -it inspiring_lovelace bash
    ```
    - **inspiring_lovelace** ist nur ein Beispiel. Sie müssen den passenden Namen des Containers auswählen.

- Führen Sie die Tests aus:
     ```bash
    pytest
    ```

## Protokollierung

Die Anwendung protokolliert wichtige Ereignisse in einer Datei namens `api.log`, die sich im Projektverzeichnis befindet. Die Protokolldatei erfasst empfangene Anfragen, Validierungsfehler und getroffene Vorhersagen.

## To-do

1. [ ] Verbesserung der Anfrageverarbeitung (Validierung und Vorverarbeitung der Eingabedaten)
2. [ ] Skalierbarkeitsaspekten wie z.B. Caching-Mechanismen
3. [ ] Hinzufügen einer Swagger-Dokumentation
4. [ ] Hinzufügen weiterer Logiktests


# Coding Challenge MLE

## Introduction

The proposed application extracts sentiment-related information from text, focusing on the subtext, and analyzes sentiment.

## Installation

- Clone this repository to your local machine:

    ```bash
    git clone https://github.com/NadiaSbaa/CodingChallenge_MLE.git
    ```

- Navigate to the project directory:

    ```bash
    cd CodingChallenge_MLE
    ```

### Build and Run


- Build the Docker image:
     ```bash
    docker build -t sentiment_text_extractor .
    ```
  - **sentiment_text_extractor** is an example. You can choose a different name.


- Run the Docker container:
     ```bash
    docker run -p 8000:8000 sentiment_text_extractor .
    ```

### Endpoints

- **GET /predict**: Predicts predict text that express sentiment-related information from provided text and sentiment.

    - **Request Parameters**:
        - `text` (string): The input text for sentiment analysis.
        - `sentiment` (string): The sentiment type to analyze (`positive`, `negative`, or `neutral`).

    - **Example Request**:
        ```bash
        curl -X GET -H "Content-Type: application/json" -d '{"text": "I love this product", "sentiment": "positive"}' http://localhost:8000/predict
        ```

    - **Example Response**:
        ```json
        {"selected_text": "love"}
        ```
  - **Error Handling**:
      - If `text` parameter is missing or empty:
          - Response: `400 Bad Request`
          - Error Message: `Missing / Empty parameter: text`

      - If `sentiment` parameter is missing or empty:
          - Response: `400 Bad Request`
          - Error Message: `Missing / Empty parameter: sentiment`

      - If `sentiment` parameter value is invalid:
          - Response: `400 Bad Request`
          - Error Message: `Invalid sentiment value. Sentiment can be positive, negative or neutral`

### Test


- Execute within the Docker container:
     ```bash
    docker exec -it inspiring_lovelace bash
    ```
    - **inspiring_lovelace** is an example. You need to select the adequate name of the container.

- Run tests:
     ```bash
    pytest
    ```



## Logging

The application logs important events to a file named `api.log` located in the project directory. The log file captures requests received, validation errors, and predictions made.
E

## To do

1. [ ] Improove Request Processing (Validate and preprocess the input data )
2. [ ] Consideration of scalability aspects such and caching mechanisms
3. [ ] Add a Swagger documentation
4. [ ] Add more logic tests
