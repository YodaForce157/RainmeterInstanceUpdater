# How to use

Change the folder variable to the path of your minecraft instances and the configFile variable with your rainmeter ini path, and then run the file, this should update your ini file with a section for each minecraft instance.
To add values to the ini file sections, under line 24 you can add `write_config.set(sectionName, "valueName", "value")` for each value you would like to add.

The blacklist array is for stopping certain folders from being added.
