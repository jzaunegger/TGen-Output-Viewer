# TGen-Output-Viewer
A basic python script that allows you to view the output sentences from Text Generationg using the TGen Model for the E2E Challenge. 

This script reads .txt files from the 'dataset' directory location at the root of the repository. Here you can place the output text files from the Text Generation process of the TGen model. The program will ask you to enter a number, and will take that number and print out the sentence whose line number matches the input number. It is a very simple program using no dependencies besides built-in python modules. 

Provided is some sample data that uses a varying number of passes during training. In the filename there are various flags that describe what the file is:
  * #s - The number of passes to be used during the Training and Generation Stages.
  * t# - The trial number with that pass count.
