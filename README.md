# AVEVA Alarm Extractor

Converts Aveva EDGE alarm files (.alh) to excel


## Istallation

#### Windows

- Installation on windows

#### Linux

- Installation on linux



### Help

In windows you might encounter an error with setuptools while running `poetry install` command. To fix this, you need to enable long path by exceuting the following command in Windows powershell.

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

You can read more about this [here](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later "Enabling long path in window 10")
