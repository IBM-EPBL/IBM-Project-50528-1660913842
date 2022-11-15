{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "GiRQ27X4JRcH"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data=pd.read_excel(\"/content/Crude Oil Prices Daily.xlsx\")"
      ],
      "metadata": {
        "id": "dbaHUfMiJW8I"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.isnull().any()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RAUyZB0-Jp0t",
        "outputId": "9f1ec869-c35f-4764-8989-0d5d82646e18"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Date             False\n",
              "Closing Value     True\n",
              "dtype: bool"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yorF39lCJsyV",
        "outputId": "4001984b-54cc-4b54-f73b-926ff03ac00f"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Date             0\n",
              "Closing Value    7\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.dropna(axis=0,inplace=True)"
      ],
      "metadata": {
        "id": "g3FWuWVPJwms"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vIHbyOs4JzIf",
        "outputId": "47f79e73-6c7b-4d04-a0bd-09ae39d18bcf"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Date             0\n",
              "Closing Value    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data_oil=data.reset_index()['Closing Value']\n",
        "data_oil"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IoxUNwrvJ2b6",
        "outputId": "2011717f-466c-4af2-973c-3980b6229a4d"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       25.56\n",
              "1       26.00\n",
              "2       26.53\n",
              "3       25.85\n",
              "4       25.87\n",
              "        ...  \n",
              "8211    73.89\n",
              "8212    74.19\n",
              "8213    73.05\n",
              "8214    73.78\n",
              "8215    73.93\n",
              "Name: Closing Value, Length: 8216, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import MinMaxScaler\n",
        "scaler=MinMaxScaler(feature_range=(0,1))\n",
        "data_oil=scaler.fit_transform(np.array(data_oil).reshape(-1,1))"
      ],
      "metadata": {
        "id": "5m-DUFI9J_WN"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data_oil"
      ],
      "metadata": {
        "id": "fyMwOo1jKLqL",
        "outputId": "6e2bdf01-77aa-4e93-f117-6ab963e21c0a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.11335703],\n",
              "       [0.11661484],\n",
              "       [0.12053902],\n",
              "       ...,\n",
              "       [0.46497853],\n",
              "       [0.47038353],\n",
              "       [0.47149415]])"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    }
  ]
}