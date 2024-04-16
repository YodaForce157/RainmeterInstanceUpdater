import os
import configparser

folder = 'instances folder'
instances = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
blacklist = ['.LAUNCHER_TEMP', '.tmp']
blacklistSet = set(blacklist)
configFile = 'YourConfig.iniFilePath'
i=0

def DeleteInstanceSections(configFile):
    curr_config = configparser.ConfigParser(strict=False)
    curr_config.read(configFile, encoding="utf-16")
    for sections in curr_config.sections():
        if sections.startswith("INSTANCE-") == True:
            curr_config.remove_section(sections)
    with open(configFile, "w", encoding="utf-16") as fp:
        curr_config.write(fp)
        fp.close()

def CreateInstanceImage(instanceN):
    write_config = configparser.ConfigParser()
    sectionName = f"INSTANCE-{instanceN}"
    write_config.add_section(sectionName)

    return write_config

DeleteInstanceSections()

for instance in instances:
    instanceInBlacklist = instance in blacklistSet
    if not instanceInBlacklist:
        with open(configFile, "a", encoding="utf-16") as fp:
            CreateInstanceImage(instance).write(fp)
            i = i + 1
            fp.close()
