Welcome to the **OPENLABS Employee Enrolment System** wiki!

This wiki is the main source of documentation for OPENLABS Employee Enrolment System. 

**Quick Introduction**

Employee Enrolment System is an open source project that creates and maintains all the details of its employees i.e. Personal Details, Educational Details.

**Technology Stack**

* Tryton 3.4
* Postgress 9.3.6

**Prerequisites**<br/>
1. Install virtualenvwrapper
   `pip install virtualenvwrapper`<br />
2. Install postgress 9.3.6
   `sudo apt-get install postgresql postgresql-contrib`

**Steps Involved**<br />
1. Install cookiecutter `pip install cookiecutter` .<br /> Cookiecutter is a template for Tryton module boilerplate.<br /><br />
2. Generate a Tryton module :<br /> `cookiecutter https://github.com/openlabs/trytond-cookiecutter.git` .<br /><br />
More details @ [Cookiecutter](https://github.com/openlabs/trytond-cookiecutter)<br /><br />
3. Create a configuration file globally according to your requirements. More details for writing your configuration file can be viewed at this gist : [Tryton 3.4 Configuration File(Sample)](https://gist.github.com/sharoonthomas/0b425318b47b3dc999e1)<br />You need to update your super password in your configuration file with the help of the following command : <br /> `$ python -c 'import getpass,crypt,random,string;<br />
print crypt.crypt(getpass.getpass(),"".join(random.sample(string.ascii_letters + string.digits, 8)))'`<br /><br />
4. I have created two classes 'PersonalDetails' and 'Education' in my `test.py` model and used Party module of trytond as the base class for PersonalDetails.<br /><br />
5. Further, I created a `test.xml` file and designed two forms and two tree views for my classes. I have divided the views into pages and notebooks to bring out a rich user experience.<br /><br />
6. You also need to update your `__init__.py` and `tryton.cfg` with suitable class names and views and register them in the Pool.<br /><br />
7. After writing all the views and models the following commands are used to update both tryton client and python.<br />
 `trytond -c [path-to-your-config-file] -u module-name -d database-name`<br />
 `pip install -U --no-deps .`<br /><br />
8. Lastly, launch the server and tryton client with the following commands :<br />
  `trytond -c [path-to-your-config-file]`
  `tryton -dv` 
