# [82/1948 Ranked Leaderboard](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-reduce-marketing-spend/leaderboard/reduce-marketing-waste-24-9c4e0592/page/2/)

## [Code](./reduce_marketing_waste_cat_boost.ipynb)

# Reduce Marketing Waste

![feature image](./images/reduce-marketing-waste-feature-image.png)

# [Competition Link - My Leaderboard](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-reduce-marketing-spend/leaderboard/reduce-marketing-waste-24-9c4e0592/page/2/)

![leaderboard](./images/leaderboard.png)


## [HackerEarth Reduce Marketing Waste](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-reduce-marketing-spend/)
> Mar 31, 2021, 10:00 PM IST - Apr00 30, 2021, 10:30 PM IST

## **Problem**

<div class="description">
	<p>You want to reduce marketing waste and aim your marketing initiatives only at those customers who will
		benefit from your product. This will result in the following:
	</p>
	<ul>
		<li>Increased business</li>
		<li>New customers who are compatible with your organization</li>
		<li>Seamless transactions with a higher success rate</li>
		<li>More profit with fewer obstacles</li>
	</ul>
	<h2 style="text-align:justify"><strong>Task</strong></h2>
	<p style="text-align:justify">Your company has&nbsp;products that can be used for hiring
		assessments.&nbsp;Your task is to predict the probability percentage that a client will purchase a
		product from the features provided in the dataset that is given.
	</p>
	<h2>Dataset description</h2>
	<p>The dataset folder contains the following files:</p>
	<ul>
		<li><strong>train.csv</strong>: 7007 x 23</li>
		<li><strong>test.csv</strong>: 2093 x 22</li>
		<li><strong>sample_submission.csv</strong>: 5 x 2</li>
	</ul>
	<p>The columns provided in the dataset are as follows:</p>
	<table border="1" style="width:500px">
		<tbody>
			<tr>
				<td style="text-align:center; width:139px"><strong>Column name</strong></td>
				<td style="text-align:center; width:346px"><strong>Description</strong></td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Deal_title</td>
				<td style="width:346px">Represents a unique title for each deal</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Lead_name</td>
				<td style="width:346px">Represents the name of a lead</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Industry</td>
				<td style="width:346px">Represents the industry that a lead belongs to</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Deal_value</td>
				<td style="width:346px">Represents the value of a deal between a lead and your company (in
					Dollars)
				</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Weighted_amount</td>
				<td style="width:346px">Represents a value that is&nbsp;estimated&nbsp;revenue&nbsp;times a
					probability
				</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Date_of_creation</td>
				<td style="width:346px">Represents the date when a deal's pipeline was created</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Pitch</td>
				<td style="width:346px">Represents the different types of products that your company offers to a
					lead
				</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Contact_no</td>
				<td style="width:346px">Represents the contact details of a lead (masked)</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Lead_revenue</td>
				<td style="width:346px">Represents the lead company's revenue (in Dollars)</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Fund_category</td>
				<td style="width:346px">Represents the type of funding that a lead possesses</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Geography</td>
				<td style="width:346px">Represents the geographical location of a lead (country)</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Location</td>
				<td style="width:346px">Represents the geographical location of a lead (state or city)</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">POC_name</td>
				<td style="width:346px">Represents the lead's point of contact's name</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Designation</td>
				<td style="width:346px">Represents the lead POC's designation</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Lead_POC_email</td>
				<td style="width:346px">Represents the lead POC's email address</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Hiring_candidate_role</td>
				<td style="width:346px">Represents the job role that a lead wants to hire&nbsp;</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Lead_source</td>
				<td style="width:346px">Represents the source from which the lead is generated</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Level_of_meeting</td>
				<td style="width:346px">
					<p>Represents the level of a meeting with the lead.&nbsp;</p>
					<ul>
						<li>Level 1: Introductory call</li>
						<li>Level 2: Demo call</li>
						<li>Level 3: Pre-sales call</li>
					</ul>
				</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Last_lead_update</td>
				<td style="width:346px">Represents the communication update between a lead and your company</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Internal_POC</td>
				<td style="width:346px">Represents the name of the employee who has generated the lead</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Resource</td>
				<td style="width:346px">Represents whether your company has enough resources to satisfy a lead's
					requirements
				</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Internal_rating</td>
				<td style="width:346px">Represents a rating (1-5) given to a lead&nbsp;</td>
			</tr>
			<tr>
				<td style="text-align:center; width:139px">Success_probability</td>
				<td style="width:346px">Represents the probability that a lead will buy a product or
					onboard&nbsp;
				</td>
			</tr>
		</tbody>
	</table>
	<h2><strong>Evaluation metric</strong></h2>
	<pre
		class="prettyprint"><code>score = max(0, 100-np.sqrt(metrics.mean_squared_error(actual, predicted)))</code></pre>
	<h2><strong>Result submission guidelines</strong></h2>
	<ul>
		<li>The index is <strong>Deal_title</strong> and the target is
			the&nbsp;<strong>Success_probability</strong> column.&nbsp;
		</li>
		<li>The submission file must be submitted in <strong>.csv</strong> format only.</li>
		<li>The size of this submission file must be&nbsp;2093 x&nbsp;2.</li>
	</ul>
	<p><strong>Note</strong>: Ensure that your submission file contains the following:</p>
</div>