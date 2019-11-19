# Extract Byonic parameters to Prose

This parses ProteinMetrics' Byonic parameter files .byparms into plain text as prose. After activating the correct Python environment or virtual environment, you can run extract_byonic_params.py as:

~~~
python extract_byonic_params.py
~~~

Or you can just run the EXE from Windows.


# Python requirements

1. Python 3.6
2. pandas
3. tkinter (this script opens a GUI, which I believe only works in Windows and you install it with Python at the install screen)

# Windows Binary Security

Algorithm : SHA256

Hash      : BA57B97C088FFA510CAADDE3FE95F37DD195AEE5B1017DBE5F0D7CC61FAE1D0F

Path      : extractbyonic\extract_byonic_params.exe

You can check the SHA-256 of the binary that you download by running in Windows Powershell:

~~~
Get-FileHash .\extract_byonic_params.exe
~~~
