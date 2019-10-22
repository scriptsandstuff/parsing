# Automated extraction of historic geographic boundaries from current boundaries and preceeding Acts of Parliment.
I am unable to find gemoetry data for Dail constituency boundaries prior to the Electoral Act 2009. The obvious solution is to ask if those geometries are available form the CSO or Osi but there is a way they can be recreated.

Constituencies change over time as population changes. Constituencies are each made up of a grouping of Electoral Divisions. Electoral Divisions have a constant geometry; in general\*. Therefore, if we have the geometry of the Electoral Divisions and we know the Divisions in each group we can create the geometry for the constituencies.

We find the divisons in each constituency in the Act of Parliment. The schedule of the Acts contain a table of constituencies. Each constitunecy is described. What we require is a list. We notice astonishing, almost robotic consistency in the constituency descriptions. We believe we can automate the creation of the necessary list. 

See [Act2017.pdf](https://github.com/scriptsandstuff/parsing/blob/master/Act2017.pdf) for the 2017 Act.
See [constituencies_bin.py](https://github.com/scriptsandstuff/parsing/blob/master/constituencies_bin.py) for the regular expressions.
See [schedule_DF.csv](https://github.com/scriptsandstuff/parsing/blob/master/schedule_DF.csv) for the extracted data.
Matching and grouping is incomplete, in a complete mess and spread across the ipy notebooks.

\* Electoral Division boundaries do change. For example, sometimes they change when a city or town boundary changes. Those changes are contained in Local Government Acts and have yet to be considered.