{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
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
      "execution_count": null,
      "metadata": {
        "id": "gMYdEoHq-oKE"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data=pd.read_excel(\"/content/Crude Oil Prices Daily.xlsx\")"
      ],
      "metadata": {
        "id": "gmhtVZLW_Ghh"
      },
      "execution_count": null,
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
        "id": "N-TTvICd_RdY",
        "outputId": "553b761b-7f2e-4141-d253-ccca37df751a"
      },
      "execution_count": null,
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
          "execution_count": 5
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
        "id": "XZ2t4xPq_Wan",
        "outputId": "12bd5fba-2625-43b1-85d2-48ed44149251"
      },
      "execution_count": null,
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
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.dropna(axis=0,inplace=True)"
      ],
      "metadata": {
        "id": "5Td0P9d2_aKw"
      },
      "execution_count": null,
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
        "id": "E4xiOaaP_hLy",
        "outputId": "5a082030-aeb2-4686-b991-0c47f814d67b"
      },
      "execution_count": null,
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
          "execution_count": 8
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
        "id": "hCIMsLTG_mLH",
        "outputId": "e2174bb8-b283-419b-c5d3-d7e9ffa55e5a"
      },
      "execution_count": null,
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
          "execution_count": 9
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
        "id": "nJPq_3ep_xE-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data_oil"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SYKkDj5vAHem",
        "outputId": "1a0cd460-f0fa-4048-b747-bd3ed93e1fac"
      },
      "execution_count": null,
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
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.plot(data_oil)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "NEJmc3gQAJ5F",
        "outputId": "43f960c9-7748-47e1-d218-5f4c4d91cb16"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f2e8aae7250>]"
            ]
          },
          "metadata": {},
          "execution_count": 12
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "training_size=int(len(data_oil)*0.65)\n",
        "test_size=len(data_oil)-training_size\n",
        "train_data,test_data=data_oil[0:training_size,:],data_oil[training_size:len(data_oil),:1]"
      ],
      "metadata": {
        "id": "C9pYgejLAPns"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "training_size,test_size"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k89wWlnmAo6U",
        "outputId": "af336bcf-8a8e-4389-c233-ac26c57a61c1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5340, 2876)"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train_data.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hvzEBVyUAr-T",
        "outputId": "a356f237-c919-4164-e01f-a7463275449c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5340, 1)"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def create_dataset(dataset,time_step=1):\n",
        "  dataX,dataY=[],[]\n",
        "  for i in range(len(dataset)-time_step-1):\n",
        "    a=dataset[i:(i+time_step),0]\n",
        "    dataX.append(a)\n",
        "    dataY.append(dataset[i+time_step,0])\n",
        "  return np.array(dataX),np.array(dataY)"
      ],
      "metadata": {
        "id": "-YpjHQdPAu1r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "time_step=10\n",
        "x_train,y_train=create_dataset(train_data,time_step)\n",
        "x_test,y_test=create_dataset(test_data,time_step)"
      ],
      "metadata": {
        "id": "DDWunzVjBOs0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(x_train.shape),print(y_train.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5hHUEc_WBhOZ",
        "outputId": "aea25456-6e97-40fe-ebae-33153be8ec20"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(5329, 10)\n",
            "(5329,)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(None, None)"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(x_test.shape),print(y_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-rAmRqsbBnlg",
        "outputId": "79d03fcb-a209-423c-c2a1-d240936035db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(2865, 10)\n",
            "(2865,)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(None, None)"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x_train"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zd-z5Ib8BwGP",
        "outputId": "90542887-8fc2-458c-b22e-929f8c0bd41c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.11335703, 0.11661484, 0.12053902, ..., 0.10980305, 0.1089886 ,\n",
              "        0.11054346],\n",
              "       [0.11661484, 0.12053902, 0.11550422, ..., 0.1089886 , 0.11054346,\n",
              "        0.10165852],\n",
              "       [0.12053902, 0.11550422, 0.1156523 , ..., 0.11054346, 0.10165852,\n",
              "        0.09906708],\n",
              "       ...,\n",
              "       [0.36731823, 0.35176958, 0.36080261, ..., 0.36391234, 0.37042796,\n",
              "        0.37042796],\n",
              "       [0.35176958, 0.36080261, 0.35354657, ..., 0.37042796, 0.37042796,\n",
              "        0.37879461],\n",
              "       [0.36080261, 0.35354657, 0.35295424, ..., 0.37042796, 0.37879461,\n",
              "        0.37916482]])"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x_train=x_train.reshape(x_train.shape[0],x_train.shape[1],1)\n",
        "x_test=x_test.reshape(x_test.shape[0],x_test.shape[1],1)"
      ],
      "metadata": {
        "id": "BsJsc-dzBzPI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.models import Sequential\n",
        "from tensorflow.keras.layers import Dense\n",
        "from tensorflow.keras.layers import LSTM"
      ],
      "metadata": {
        "id": "Nti1iMdXCFHH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model=Sequential()"
      ],
      "metadata": {
        "id": "5Bbk8sA6CWWd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.add(LSTM(50,return_sequences=True,input_shape=(10,1)))\n",
        "model.add(LSTM(50,return_sequences=True))\n",
        "model.add(LSTM(50))"
      ],
      "metadata": {
        "id": "gciW66VECcKl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.add(Dense(1))"
      ],
      "metadata": {
        "id": "PI_o_1SNC0jV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y_QQbjo2C7z0",
        "outputId": "ecd997a8-231d-4d4c-c495-fc020a381466"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " lstm (LSTM)                 (None, 10, 50)            10400     \n",
            "                                                                 \n",
            " lstm_1 (LSTM)               (None, 10, 50)            20200     \n",
            "                                                                 \n",
            " lstm_2 (LSTM)               (None, 50)                20200     \n",
            "                                                                 \n",
            " dense (Dense)               (None, 1)                 51        \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 50,851\n",
            "Trainable params: 50,851\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model.compile(loss='mean_squared_error',optimizer='adam')"
      ],
      "metadata": {
        "id": "9-EcjJXFDAvc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=3,batch_size=64,verbose=1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jmk2fEa4DItV",
        "outputId": "5533ed7e-ab81-4b5a-a0bb-e86e0399a05d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/3\n",
            "84/84 [==============================] - 6s 25ms/step - loss: 0.0017 - val_loss: 0.0011\n",
            "Epoch 2/3\n",
            "84/84 [==============================] - 1s 16ms/step - loss: 1.2375e-04 - val_loss: 7.8338e-04\n",
            "Epoch 3/3\n",
            "84/84 [==============================] - 1s 16ms/step - loss: 1.2058e-04 - val_loss: 7.5010e-04\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.callbacks.History at 0x7f2e2b3da490>"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##Transformback to original form\n",
        "train_predict=scaler.inverse_transform(train_data) \n",
        "test_predict=scaler.inverse_transform(test_data)\n",
        "### Calculate RMSE performance metrics\n",
        "import math \n",
        "from sklearn.metrics import mean_squared_error\n",
        "math.sqrt(mean_squared_error(train_data,train_predict))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vtdx97vxH4hF",
        "outputId": "dd7ecc10-c73c-4005-f15b-4bdfc7d710f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "29.347830443269938"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.models import load_model"
      ],
      "metadata": {
        "id": "BBanpJ69H6Hh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.save(\"crude_oil.hs\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jYCE9HozIqOa",
        "outputId": "8d32e61b-d127-4314-9645-234793b3be28"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:absl:Found untraced functions such as lstm_cell_layer_call_fn, lstm_cell_layer_call_and_return_conditional_losses, lstm_cell_1_layer_call_fn, lstm_cell_1_layer_call_and_return_conditional_losses, lstm_cell_2_layer_call_fn while saving (showing 5 of 6). These functions will not be directly callable after loading.\n",
            "WARNING:absl:<keras.layers.recurrent.LSTMCell object at 0x7f2e2f939a10> has the same name 'LSTMCell' as a built-in Keras object. Consider renaming <class 'keras.layers.recurrent.LSTMCell'> to avoid naming conflicts when loading with `tf.keras.models.load_model`. If renaming is not possible, pass the object in the `custom_objects` parameter of the load function.\n",
            "WARNING:absl:<keras.layers.recurrent.LSTMCell object at 0x7f2e2b60bf90> has the same name 'LSTMCell' as a built-in Keras object. Consider renaming <class 'keras.layers.recurrent.LSTMCell'> to avoid naming conflicts when loading with `tf.keras.models.load_model`. If renaming is not possible, pass the object in the `custom_objects` parameter of the load function.\n",
            "WARNING:absl:<keras.layers.recurrent.LSTMCell object at 0x7f2e2b510cd0> has the same name 'LSTMCell' as a built-in Keras object. Consider renaming <class 'keras.layers.recurrent.LSTMCell'> to avoid naming conflicts when loading with `tf.keras.models.load_model`. If renaming is not possible, pass the object in the `custom_objects` parameter of the load function.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "### Plotting\n",
        "look_back=10\n",
        "trainpredictPlot = np.empty_like(data_oil)\n",
        "trainpredictPlot[:, :]= np.nan\n",
        "trainpredictPlot[look_back:len(train_predict)+look_back, :] = train_predict\n",
        "# shift test predictions for plotting\n",
        "testPredictplot = np.empty_like(data_oil)\n",
        "testPredictplot[:,: ] = np.nan\n",
        "testPredictplot[look_back:len(test_predict)+look_back, :] = test_predict\n",
        "# plot baseline and predictions\n",
        "plt.plot(scaler.inverse_transform(data_oil))\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "L-6vXuAYJkcu",
        "outputId": "c930fefd-934e-4926-89ab-930666200083"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(test_data)"
      ],
      "metadata": {
        "id": "g_YckjXtLJNC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d81bb2c6-e49a-42c1-cdb3-b5145a73c130"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2876"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x_input=test_data[2866:].reshape(1,-1)\n",
        "x_input.shape"
      ],
      "metadata": {
        "id": "RgawVIleLW-v",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "84eceae5-f4e4-4376-fbb8-9714c26300c4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1, 10)"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "temp_input=list(x_input) \n",
        "temp_input=temp_input[0].tolist()"
      ],
      "metadata": {
        "id": "1g1Iu241LcWh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "temp_input"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "529unKThLeVQ",
        "outputId": "135943b3-ea30-4d6c-fe1d-5beea39a94bc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0.44172960165852215,\n",
              " 0.48111950244335855,\n",
              " 0.49726047682511476,\n",
              " 0.4679401747371539,\n",
              " 0.4729749740855915,\n",
              " 0.47119798608026064,\n",
              " 0.47341922108692425,\n",
              " 0.4649785280616022,\n",
              " 0.4703835332444839,\n",
              " 0.47149415074781587]"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lst_output=[]\n",
        "n_steps=10\n",
        "i=0\n",
        "while(i<10):\n",
        "    if(len(temp_input)>10):\n",
        "#print(temp_input)\n",
        "       x_input=np.array(temp_input[1:]) \n",
        "       print(\"{} day input {}\".format(i,x_input))\n",
        "       x_input=x_input.reshape(1,-1)\n",
        "       x_input = x_input.reshape((1, n_steps, 1)) #print(x_input)\n",
        "       yhat = model.predict(x_input, verbose=0)\n",
        "       print(\"{} day output {}\".format(i,yhat))\n",
        "       temp_input.extend(yhat[0].tolist())\n",
        "       temp_input=temp_input[1:] #print(temp_input)\n",
        "       lst_output.extend(yhat.tolist())\n",
        "       i=i+1\n",
        "    else:\n",
        "       x_input = x_input.reshape((1, n_steps,1))\n",
        "       yhat = model.predict(x_input, verbose=0)\n",
        "       print(yhat[0])\n",
        "       temp_input.extend(yhat[0].tolist()) \n",
        "       print(len(temp_input))\n",
        "       lst_output.extend(yhat.tolist())\n",
        "       i=i+1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ULCbP4K1LlBQ",
        "outputId": "6947d757-5897-4056-d132-215b0b9e2843"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0.47442466]\n",
            "11\n",
            "1 day input [0.4811195  0.49726048 0.46794017 0.47297497 0.47119799 0.47341922\n",
            " 0.46497853 0.47038353 0.47149415 0.47442466]\n",
            "1 day output [[0.47781762]]\n",
            "2 day input [0.49726048 0.46794017 0.47297497 0.47119799 0.47341922 0.46497853\n",
            " 0.47038353 0.47149415 0.47442466 0.47781762]\n",
            "2 day output [[0.47653615]]\n",
            "3 day input [0.46794017 0.47297497 0.47119799 0.47341922 0.46497853 0.47038353\n",
            " 0.47149415 0.47442466 0.47781762 0.47653615]\n",
            "3 day output [[0.47364426]]\n",
            "4 day input [0.47297497 0.47119799 0.47341922 0.46497853 0.47038353 0.47149415\n",
            " 0.47442466 0.47781762 0.47653615 0.47364426]\n",
            "4 day output [[0.47442248]]\n",
            "5 day input [0.47119799 0.47341922 0.46497853 0.47038353 0.47149415 0.47442466\n",
            " 0.47781762 0.47653615 0.47364426 0.47442248]\n",
            "5 day output [[0.47467044]]\n",
            "6 day input [0.47341922 0.46497853 0.47038353 0.47149415 0.47442466 0.47781762\n",
            " 0.47653615 0.47364426 0.47442248 0.47467044]\n",
            "6 day output [[0.47518066]]\n",
            "7 day input [0.46497853 0.47038353 0.47149415 0.47442466 0.47781762 0.47653615\n",
            " 0.47364426 0.47442248 0.47467044 0.47518066]\n",
            "7 day output [[0.47546706]]\n",
            "8 day input [0.47038353 0.47149415 0.47442466 0.47781762 0.47653615 0.47364426\n",
            " 0.47442248 0.47467044 0.47518066 0.47546706]\n",
            "8 day output [[0.4767432]]\n",
            "9 day input [0.47149415 0.47442466 0.47781762 0.47653615 0.47364426 0.47442248\n",
            " 0.47467044 0.47518066 0.47546706 0.47674319]\n",
            "9 day output [[0.47736228]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "day_new=np.arange(1,11) \n",
        "day_pred=np.arange(11,21)\n",
        "len(data_oil)\n",
        "plt.plot(day_new, scaler.inverse_transform(data_oil[8206:])) \n",
        "plt.plot(day_pred, scaler.inverse_transform(lst_output))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "0O0jGgIjL67v",
        "outputId": "c2e74268-f353-4dcb-b101-b9421d92ae59"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f2e26c59e50>]"
            ]
          },
          "metadata": {},
          "execution_count": 38
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df3=data_oil.tolist() \n",
        "df3.extend(lst_output) \n",
        "plt.plot(df3[8100:])"
      ],
      "metadata": {
        "id": "SR0uR3ytMD7f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "outputId": "3f10071c-24cf-4b39-9fc4-0a60aefbb4bc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f2e26bec890>]"
            ]
          },
          "metadata": {},
          "execution_count": 39
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df3=scaler.inverse_transform(df3).tolist()"
      ],
      "metadata": {
        "id": "qVvbsTl2MHyJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.plot(scaler.inverse_transform(data_oil))"
      ],
      "metadata": {
        "id": "fY2QI3mJRQfn",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "outputId": "6646f50f-420a-4a99-bb86-e47562b84513"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f2e25114490>]"
            ]
          },
          "metadata": {},
          "execution_count": 41
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}