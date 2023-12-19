from github import Github

# 替换为你的个人访问令牌
token = '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'

# 替换为你要查询的组织名称
organization_name = 'X-lab2017'

# 创建 Github 对象并进行身份验证
g = Github(token)

# 获取组织对象
org = g.get_organization(organization_name)

# 获取组织的所有仓库
repos = org.get_repos()

# 遍历并打印组织的所有仓库名称
for repo in repos:
    print(repo.name)