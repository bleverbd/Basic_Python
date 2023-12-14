### Git Command <br>
git config --global user.name "your_username" <br>
git config --global user.email "your_useremail" <br>

### Jupyter Notebook Path Change<br>
1.Goto anaconda Command Powershell Prompt<br>
    jupyter notebook --generate-config<br>
2.Goto Jupyter Notebook and check Current Path<br>
   &nbsp;&nbsp;import os <br>
    &nbsp;&nbsp;print(os.getcwd()) <br>
3.Goto this Path from 2 number Step<br>
    &nbsp;1.Open .jupyter Folder <br>
    &nbsp;2.Open jupyter_notebook_config.py with Visual Studio <br>
    &nbsp;3.Search(Ctrl + F) notebook_dir <br>
    &nbsp;4.="Enter Path" and Remove Comment<br>
    &nbsp;5.Save and Exit<br>
4.Resart Jupyter Notebook and Check  <br>