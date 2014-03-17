Testing possible bugs in Django 1.7a2 migrations.

Specifically, there seems to be an issue creating foreign keys to proxy models. 
 - Creating the makemigrations works, but running the actual migration with the new migrate command results in an error where Django complains that the proxy model cannot be resolved. 
