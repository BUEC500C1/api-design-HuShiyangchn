# api-design-HuShiyangchn
## Introduction
In this module, you can get the brief introduction about the airport and the current weather information about the airport. The information is fetched from Openweathermap API.
And the information is packaged in api interface which is implemented by tornado module.
## Implementation
<<<<<<< HEAD
First I generated a file inlcuded all information about US airport based on airport-codes.csv which is produced by @svetozarstojkovic. More information about the file can be found in https://github.com/datasets/airport-codes. Then the program could provide short introduction about the airport and find the precise coordinates based on this file. Then the program can use the coordinates to call the API and get the precise weather information.</br>

And all these will be packaged into a api interface, you can get the information like the example below.
## Example
Run the program by type ```python3 weatherapi.py```  </br>
Then you will start to run a web service.</br>
To get the information from api please the following address in you browser:</br>
```"Your ip address":8888/?id = "the airport you are searching for```</br>
For example:</br>
The ip address of my computer is 10.0.0.86. So I type the address:</br>
```http://10.0.0.86:8888/?id=General Edward Lawrence Logan International Airport ```</br>
Attendition: Please use full name of airport in the csv file.</br>
Then we can get return like this:</br>

=======
First I generated a file inlcuded all information about US airport based on airport-codes.csv which is produced by @svetozarstojkovic. More information about the file can be found in https://github.com/datasets/airport-codes. Then the program could provide short introduction about the airport and find the precise coordinates based on this file. Then the program can use the coordinates to call the API and get the precise weather information.
## Example
Run the program by type ```python3 weatherapi.py```
After running you should enter the name of the airport:
![image](https://github.com/BUEC500C1/api-design-HuShiyangchn/blob/master/Images/1.png)
Then you can see the brief introduction and the weather information of the airport:
![image](https://github.com/BUEC500C1/api-design-HuShiyangchn/blob/master/Images/2.png)
>>>>>>> ba460fd0d1e43d36986c5be8cedf7f4c5466e470
