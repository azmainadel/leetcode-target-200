class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def getKey(log):
            identifier, content = log.split(' ', maxsplit=1)
            if content.split(' ')[0].isdigit():
                return (1, None, None)
            else:
                return (0, content, identifier)

        return sorted(logs, key=getKey)