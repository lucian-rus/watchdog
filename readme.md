> in work

right now this generates two files:
* groups.csv -> contains all groups and links to them
* members.csv -> contains each member and links to it

---------------------------------------------------------

political aggregator for the romanian senate and deputy chambers
* scrape senate page 
    * get all parties
    * get all members from each party
    * get their biography
    * get their electronic votes and the laws they voted on
* scrape deputy chamber page

---------------------------------------------------------

todo:
* get biography and additional data
* get voting data
* update readme
* provide usage instructions

step 1.
scrape "https://www.senat.ro/EnumGrupuri.aspx" for ".nsnt-group-card__name" -> get names of all groups

step 2.
go to each address from the data extracted above for ".mt-2" -> get names of all people
e.g: get "https://www.senat.ro/ComponentaGrupuri.aspx?Zi&GrupID=1042f657-ab38-4245-ac2e-9cebb90c723c" from psd card, go to it, start scraping all users

step 3.
go to each address 
e.g get "https://www.senat.ro/FisaSenator.aspx?ParlamentarID=6E681419-5F69-41CD-85CA-ACEF5EED2A63" for everyone. this is not working as intended and should be checked

first, a get call is required
all fields that need to be added in the post request are coming in the get response
as of now, this has not worked manually yet
