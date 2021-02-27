# Email-Sending-application-using-Python-Flask-in-localhost
Simple email sending application using Python Flask and Bootsrtap4 in localhost

## Simple Email sender Application

### Fameworks used : 
+ Python flask
+ Bootstrap4

### Steps :
1. Installing pip 
    + Windows: 
      ```
      py -m pip --version
      pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)

      py -m pip install --upgrade pip
      ```

    + Linux and macOS:
      ```
      python3 -m pip install --user --upgrade pip
      ```

2. Installing virtualenv
    + Windows:
      ```
      py -m pip install --user virtualenv
      ```
    + macOS and Linux:
      ```
      python3 -m pip install --user virtualenv

      ```

3. Creating a virtual environment

    +  Windows:
        ```
        py -m venv env

        ```
    +  macOS and Linux
        ```
            python3 -m venv env
        ```
    `` if in case the above one doesn't work in linux ``

        ``` 
        virtualenv --python=python3 env
        ```

4. Activating a virtual environment
    + Windows:
        ```
        .\env\Scripts\activate
        ```
    + macOS and Linux:
        ```
        source env/bin/activate
        ```

5. Installing packages

    Install below 2 packages to this project.
      ```
      pip install Flask
      ```
      ```
      pip install Flask-Mail
      ```
    
### between  step 5 or 6 ,follow anyone

6. Directly intsall from this installtion file 
      ```
      pip3 install -r installtion.txt
     ```

7. Change the setups to Run Sucessfully:
    + In app.py file 
      ```
      app.config['MAIL_USERNAME'] = 'YourMailidFromWhichYouCanSend@gmail.com'
      ```
      in above line change email from which you want to send mail. 

        ```
        app.config['MAIL_PASSWORD'] = '**********'
        ```
      in above line change password of email
    
8. To Run Application:
    ```
    python3 app.py
    ```
9. To see the Result :
    + go to web browser 
    then  Visit http://localhost:5000/

10. Important Note
    + ``
    Due to Google’s built-in security features, Gmail service may block this login attempt. You may have to decrease the security level. Visit 
    ``https://myaccount.google.com/lesssecureapps?pli=1
    `` to decrease security.
    ``
    + ``
    After running and checking working sample again change setting in `` https://myaccount.google.com/lesssecureapps?pli=1`` to earlier.
    ``
    + ``
    While running commands in linux if commands doesn't work, then use sudo before commands 
    ``
    + To output a list of package
    ```
    python3 -m pip freeze
    ```
    + To Deactivating env:
    ```
    deactivate
    ```


