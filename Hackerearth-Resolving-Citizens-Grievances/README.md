# ML-Resolving-citizens-grievances

## [152/2135 Ranked Leaderboard](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-predict-grievance-importance/leaderboard/predict-the-importance-27-a4ecaaa1/page/4/)

![Feature Image](https://media-fastly.hackerearth.com/media/hackathon/hackerearth-machine-learning-challenge-predict-grievance-importance/images/bb2de2c84b-Cover_HumanRights.jpg)

Human rights are basic rights that belong to people all around the world irrespective of race, color, sex, language, religion, political or other opinions, national or social origin, property, birth, etc. These rights include the right to life and liberty, freedom from slavery and torture, freedom of opinion and expression, the right to work and education, etc. It is meant to enable human beings to live with dignity, freedom, equality, justice, and peace. Human rights are essential to the full development of individuals and communities.

In this problem, you are given a dataset that contains grievances of various people living in a country. Your task is to predict the importance of the grievance with respect to various articles, constitutional declarations, enforcement, resources, and so on, to help the government prioritize which ones to deal with and when.

Data description
The dataset folder consists of the following three .csv files:

train.csv: Contains 8878 rows and 328 columns
test.cs: Contains 4760 rows and 327 columns
sample_submission.csv: 5 rows and 2 columns
Table description 

<table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="width:736px">
	<tbody>
		<tr>
			<td style="width:250px">
			<p style="text-align:center"><strong>Column_name</strong></p>
			</td>
			<td style="width:85px">
			<p style="text-align:center"><strong>Count</strong></p>
			</td>
			<td style="width:392px">
			<p style="text-align:center"><strong>Description</strong></p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">appno</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the application number</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">application</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the type of application used to file a complaint</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">country.alpha2</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the country code</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">country.name</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the country name</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">decisiondate</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the date on which a decision was taken</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">docname</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the case or document name</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">doctypebranch</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the type of case</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">ecli</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents an alphanumeric value that is used to identify a case</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">introductiondate</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the start date</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">itemid</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the item ID</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">judgementdate</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the judgment date</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">kpdate</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the closure date</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">languageisocode</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the language</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">originatingbody</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents a&nbsp;party or body from whom the case originated</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">originatingbody_name</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the&nbsp;name of the party of body from whom the case originated</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">originatingbody_type</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the&nbsp;type of the party of body from whom the case originated</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">parties.0</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the&nbsp;details of the party of body from whom the case originated</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">parties.1</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents the&nbsp;details of the party of body from whom the case originated</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">parties.2</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents the&nbsp;details of the party of body from whom the case originated</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">rank</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the rank (0-10000) of officials (rank of an official increases with value)</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">respondent.0</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents a respondent information</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">respondent.1</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a respondent information</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">respondent.2</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a respondent information</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">respondent.3</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a respondent information</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">respondent.4</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a respondent information</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">respondentOrderEng</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a respondent information</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">separateopinion</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the opinion on a case</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">sharepointid</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the ID of an&nbsp;opinion</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">typedescription</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents a type_description {12- 19}</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">issue.{0-26}</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">27</p>
			</td>
			<td style="width:392px">
			<p>Represents the description with respect to an issue</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">article={number}</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">47</p>
			</td>
			<td style="width:392px">
			<p>Represents the type of article with respect to a&nbsp;case</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">documentcollectionid=CASELAW</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents a document category of a case</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">documentcollectionid=JUDGMENTS</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a document category of a case</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">documentcollectionid=CHAMBER</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a document category of a case</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">documentcollectionid=ENG</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a document category of a case</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">documentcollectionid=COMMITTEE</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a document category of a case</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">documentcollectionid=GRANDCHAMBER</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">Represents a document category of a case</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">applicability={number}</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">61&nbsp;</p>
			</td>
			<td style="width:392px">
			<p>Represents the applicability of a case</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">ccl_article={Type}</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">25&nbsp;</p>
			</td>
			<td style="width:392px">
			<p>Represents the reliability of a CCL article type</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">paragraphs={number}</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">132&nbsp;</p>
			</td>
			<td style="width:392px">
			<p>Represents the reliability to a paragraph&nbsp;</p>
			</td>
		</tr>
		<tr>
			<td style="width:250px">
			<p style="text-align:center">importance</p>
			</td>
			<td style="width:85px">
			<p style="text-align:center">1</p>
			</td>
			<td style="width:392px">
			<p>Represents the importance (0-5)</p>
			</td>
		</tr>
	</tbody>
</table>

Submission format
You are required to write your predictions in a .csv file and upload it by clicking the Upload File button.

Evaluation metric
score=100×metrics.accuracy_score(actual,predicted)
