{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNIIri6IyP63EqHdSVTgBGw"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":1,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"GPyCToSjmUGh","executionInfo":{"status":"ok","timestamp":1724674402931,"user_tz":300,"elapsed":3651,"user":{"displayName":"Samuel Garcia","userId":"00938556284740834143"}},"outputId":"eb4f5786-e69a-41ed-fbc2-999a204eae5f"},"outputs":[{"output_type":"stream","name":"stdout","text":["P\n","y\n","h\n","o\n","n\n"]}],"source":["import time\n","\n","cadena= 'Python'\n","\n","for letra in cadena:\n","  if letra =='t':\n","    continue\n","  print(letra)\n","  time.sleep(1)"]}]}