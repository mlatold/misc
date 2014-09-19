XCOM-Name-Generator
===================

Parses a text file of names and randomly sorts them into an ini file that XCOM: Enemy Unknown will accept. It makes it so nobody has a first name (which isn't displayed anyway in xcom) and everyone has only last names.

I wrote this for python 3, probably works in python 2. I run a gaming youtube channel and needed to parse out over 300 names and sort them randomly, so since I'm lazy I wrote this script. It has a mirror ability incase you dont have a lot of names and want to mirror the same names to each country so you can have a big enough file.

Run it from command line like "python xcom_namegen.py". First command line argument is file (it will use names.txt if none is specified) and second argument is the ini file (uses default ini file name for xcom).