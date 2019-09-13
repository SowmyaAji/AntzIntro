# Antz Project -- An Intro

## Overview

### Vision

#### Long Term

Develop innovative methods and tools for enhanced perceptual modulation of human interaction with Information in perceptualization environments.

Given the complex and advancing nature of information gathering, there must be a more robust integration of the human user into a multipoint and immersive knowledge discovery matrix. Current information gathering and manipulation technologies are limited in their ability to support the most in-depth analysis to the extent that the human user is limited in her ability to exploit that information. We intend to develop a system sensitive in the conceptual and methodological consideration of the human’s extraordinary abilities for perception, cognition and expression. The perceptualization environment will be a multi-modal, multi-sensory, high performance communications tool for handling the escalating quantities and types of information humans will confront in the near and distant future. 

#### Near Term

Develop 3D visualization software and design methodology for constructing and perceiving meaning from hyperglyphs. The tools and methods should serve analysts exploring large data sets, especially their search for unknown, unknown patterns and anomalies. They should also serve leaders seeking to gain context, or situational awareness, in order to improve judgement.

### Background Research

David Jay Warner’s PhD thesis outlines a new way of thinking about the information exchange between machine and human. It details the theoretical underpinnings of neurocosmology, and some examples of his tangible research experiments.
Physio-informatics is defined as a systems based, physiologically robust reference architecture for designing and refining interactive human-computer interface systems in ways that increase operational throughput of information.  Extending the perceptual dimensionality of information presented to the human and enhancing the expressional capacity of the human to convey intent to the informatic system achieves this increased throughput. 

Thesis: http://projects.mindtel.com/vader/users/davew/nc-01/webphd-nc/phdavew.htm

#### Online repository of David Jay Warner projects.

MindTel: http://projects.mindtel.com/

#### Helpful Links to Understand ANTZ

#### Short brief of ANTZ and our approach
Visual Exploration Overview: https://drive.google.com/file/d/1GhYwm-Y0hRtxAP3RNodpSW6TA3gRlHeY/view?usp=sharing

##### Jeff Sales’ ANTZ visualizations
Hyperglyph Visualization Examples: http://www.edworlds.com/antz/toroids/index.php

##### Short videos showing ANTZ in motion

Introduction to ANTZ Video Tutorial: https://www.youtube.com/watch?v=Zq_8AcZXbyg
Physiometric Visualization: https://www.youtube.com/watch?v=t9mRvYxcuvU


##### Dave’s talks

Future of Data & Open Information: https://www.youtube.com/watch?v=2B6kjylnV-4
GEOINT 2018 (starts at 31:30): http://trajectorymagazine.com/sports-fans-want-data-fantasy-sports-fans-need-it/

#### ANTZ github site: 

https://github.com/openantz/antz (for cloning)

#### ANTZ user manual:

https://github.com/openantz/antz/wiki/User-Manual

#### ANTZ tutorial created by Jeff Sale:

http://www.edworlds.com/antz/toroids/tutorials/intro_lessons/index.html


### This repo: 

We have included four data sets with different kinds of data to show how to use the Antz software and how to generate glpyhs from it. 

#### How to use this repo:

Download the .exe file from the https://github.com/openantz/antz 

#### Example 1: Wellbeing

New Zealand does a country-wide survey of wellbeing and social identity measures. Here is excel and csv files of those responses and the legend. https://drive.google.com/drive/folders/1vG4BSicAiK4sFDTKPm222j14BZeL7UUz

*  From this folder, we took up two sets of data -- age-group wise wellbeing and wellbeing of different ethnicities in New Zealand. 
* We identified some major parameters to measure the wellbeing and put it into the wellbeing.csv file in the datacsv folder.
* We used the python code in wellbeinginfo.py to generate two files -- age.csv and ethnics.csv  for our Antz visualisation.

###### How to go about doing the Antz visualization of this data: 

* As the first step, we need to convert these csv files into antz node files for the software to understand it.
* We use this user interface(UI) to generate the node files: www.antzglyphs.com
* Upload the CSV file that you want to use. Please note, only column names can be strings, all the rest will be numeric values. No strings will be uploaded. We ensured that the data in our example CSV files were all numeric, except for the column names.
* At the bottom right, we need to build the template tree and map each column to each of the nodes that we want. If we click ADD, without highlighting anything, the base or root nodes will be created. If we highlight a node and click ADD, sub-nodes are generated under it. And you can have any number of such sub-nodes, and sub-nodes of sub-nodes. EDIT and REMOVE work as expected on the highlighted nodes.
* We are still working on improving this user interface. Currently, each column has to be individually clicked in the interface in the upper part of the web page and then mapped to the highlighted node by clicking MAP COLUMN.
* Once all columns are mapped, click on continue.
* Each individual node can be highlighted and mapped to color, geometry and topography. Currently we do not have a preview of the visual generated from this, but that will happen very shortly. 
* Each node has to be unclicked before clicking the next one, or all of them will have the same color, geometry and topography.
* Once the color, geometry and topography is maped for all nodes, click continue.
* The node file downloads onto your computer.
* We renamed the node files in our download folder as agegroups.csv and ethnicity.csv


##### Uploading to the visual interface

* We moved these two files into the antz-osx/antz/usr/csv folder in our downloads folder (from the github exe file -- .exe file from the https://github.com/openantz/antz -- mentioned above)
* We then double clicked on antz-osx/antz/antz file in this same downloads fodler,  which opens up the antz interface the computer.
* We type 'L' (load) and open the files [agegroups.csv, ethnicity.csv] we moved to the csv folder [antz-osx/antz/usr/csv] in the first step in this sub section. 
* The files load and the visual glyph is generated, according to the colors, shapes and topography identified by us. We have given the example glyphs generated by the above two files as ageglyph.png and EthnicityGlyph.png in our repo.


#### Example 2: USAID Developmental Data
USAID puts all its data in an open database. 
International Data and Economic Analysis database: https://idea.usaid.gov/

* We did all of the steps mentioned above and generated data relating to several countries in East Africa and put together the data in eastafrica.csv under the datacsv folder. We used eastafrica.py to generate our eastafricaresults.csv file. Again, all the data is numeric except for column names. 

* We uploaded this eastafricaresults.csv file to www.antzglyphs.com user interface, mapped columns, colors, geometry and topgraphy to generate the eafrica.csv node file, which we moved to the antz-osx/antz/usr/csv. We clicked on the antz-osx/antz/antz file and brought up the visual interface on our computer. We loaded the eafrica.csv file from the antz-osx/antz/usr/csv folder and generated the visualization eafricalifeGlyph.png

#### Example 3: Cybersecurity Data
This data set represents 58 consecutive days of de-identified event data collected from five sources within Los Alamos National Laboratory’s corporate, internal computer network.
Comprehensive, Multisource Cyber security events: https://csr.lanl.gov/data/cyber1/

* This data is already in a clean csv format and did not need the python algorithm to clean it up. However, other than the time column, all the other data is strings. What we have generated, using all of the steps mentioned above, is the representation of the various times and blips in our visualization, cyberTimeGlyph.png. This is an example of how a single data column can be visualized.









