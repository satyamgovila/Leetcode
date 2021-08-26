class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_email = {}
        
        for email in emails:
            local_name =  email.split("@")[0]
            host =  email.split("@")[1]

            local_name = local_name.split("+")[0]
            local_name = "".join(local_name.split("."))

            hash_email[email] = local_name+"@"+host
        return len(set(hash_email.values()))
        
