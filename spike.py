from git import Repo


# def get_git_repo(path):
#     return path


repo = Repo("~/workspace/hacksussex2018/")

commit_list = repo.iter_commits('master')

for i in commit_list:
    print(i.author)
    print(i.author_date)


def commit_in_week():
	pass
