from github import Github

class Collector:
    __github_api = None
    __user_name = None
    __user_repos = None
        
    def __init__(self, username, access_token):
        self.__github_api = Github(username, access_token)
        self.__user_name = username
        self.get_repositories()
        
    def get_user(self):
        return self.__github_api.get_user()
    
    def get_repositories(self): 
        try:
            self.__user_repos = self.__github_api.get_user().get_repos(self.__user_name)
        except Exception as Error:
            raise Error
            
        return self.__user_repos
    
    def get_languages(self):
        languages = []
        
        for repo in self.__user_repos:
            if not repo.language in languages and not repo.language == None:
                languages.append(repo.language)
                
        return languages
        
