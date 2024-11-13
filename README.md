# WorkflowFailureReplicationPackage
Replication script and data of "Why Do GitHub Actions Workflows Fail? An Empirical Study"

The replication-labeling file contains the result of the final categorization of the manual investigation conducted by six of the authors.

- job_id: A unique identifier assigned by us to each failed GitHub Actions job.
- url: The URL pointing to the failed GitHub Actions job. 
- project_name: The name of the project in which the GitHub Actions workflow failure occurred.
- job_name: The specific name of the job within the GitHub Actions workflow.  
- workflow_name: The name of the GitHub Actions workflow that failed. 
- step: The specific step or task in the job where the failure occurred. 
- root cause: The manually identified root cause of the failure, determined through detailed investigation. 
- sub-category-tag: Identifier for the sub category of failures
- sub-category: A more granular categorization of the failure, providing detailed insight into the nature of the root cause.
- category:  A broader classification of the failure.

The replication-surveyAnswers file contains the results of the survey conducted with GHA practitioners. The file shows the questions that were asked to the survey respondents along with the respondents' answers.

The scripts directory contains scripts used to extract the logs from failed workflows.

The data directory contains the data information used by the scripts.

