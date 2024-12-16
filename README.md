# Emotion Detection Using Liquid Neural Networks

This repository demonstrates an innovative approach to emotion detection using Liquid Neural Networks (LNNs). The project leverages the IEMOCAP dataset for model training and testing, with the aim of advancing real-time emotion recognition capabilities from audio inputs.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Preprocessing](#preprocessing)
  - [Training](#training)
  - [Model Comparison](#model-comparison)
  - [Testing](#testing)
    - [Real-time Testing](#real-time-testing)
    - [Audio File Testing](#audio-file-testing)
- [Pre-trained Models](#pre-trained-models)
- [Proof of Work](#proof-of-work)
- [Contributions](#contributions)
- [License](#license)

## Introduction

Emotion detection is crucial for numerous applications such as human-computer interaction, sentiment analysis, and mental health monitoring. This project explores Liquid Neural Networks, a novel architecture that adapts dynamically to changing inputs, making it ideal for complex tasks like emotion recognition.

## Features

- Real-time emotion detection using microphone input.
- Support for testing with pre-recorded audio files.
- Comparisons between Liquid Neural Networks and other models.
- Pre-trained models included for quick evaluation.

## Repository Structure

- **`Model_Preprocessing.ipynb`**: Preprocesses the IEMOCAP dataset to extract relevant features for training and testing.
- **`Model_Training.ipynb`**: Contains the code to train the LNN model on the preprocessed data.
- **`Model_Comparison.ipynb`**: Compares the performance of the LNN model against other baseline models.
- **`Model_Testing_realtime.ipynb`**: Enables real-time testing of the trained model using your local microphone.
- **`Model_Testing_Audio.ipynb`**: Tests the model using pre-recorded audio files.
- **`models/`**: Stores all the pre-trained models. Model filenames include accuracy in the format `xyz`, where `xyz` represents `x.yz%` accuracy (e.g., `625` for 62.5% accuracy).
- **`notebooks/`**: Contains pre-run Jupyter notebooks with outputs to showcase the proof of work.

## Requirements

- Python 3.8+
- Libraries: `tensorflow`, `numpy`, `pandas`, `librosa`, `matplotlib`

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/deadshot-21/Emotion-Detection-Using-Liquid-Neural-Networks.git
   cd Emotion-Detection-Using-Liquid-Neural-Networks
   ```
2. Download the IEMOCAP dataset (not included in this repository) and place it in the designated folder.
3. Install the required libraries using the command above.

## Usage

### Preprocessing

Run the `Model_Preprocessing.py` script to extract and prepare features from the IEMOCAP dataset.

```bash
python Model_Preprocessing.py
```

### Training

Train the LNN model by running the `Model_Training.py` script. This will generate a trained model in the `models/` directory.

```bash
python Model_Training.py
```

### Model Comparison

Use `Model_Comparison.py` to compare the trained LNN model against baseline models.

```bash
python Model_Comparison.py
```

### Testing

#### Real-time Testing

To test the model in real-time using your microphone, run:

```bash
python Model_Testing_realtime.py
```

#### Audio File Testing

To test the model using pre-recorded audio files, run:

```bash
python Model_Testing_Audio.py
```

## Pre-trained Models

Pre-trained models are available in the `models/` folder. Each model is named based on its accuracy (e.g., `625` for 62.5% accuracy). You can directly load these models for testing or further evaluation.

## Proof of Work

The `notebooks/` folder contains pre-run Jupyter notebooks with outputs to validate the methodology and results of the project.

## Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

