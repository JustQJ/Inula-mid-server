
# the trigger to github repository_dispatch action

repository_name=your_repository_name
github_token=your_github_token  #https://github.com/settings/tokens

curl -X POST ${repository_name}/dispatches  -H "Accept: application/vnd.github.everest-preview+json" -H "Authorization: ${github_token}"  --data '{"event_type": "push_hook"}'