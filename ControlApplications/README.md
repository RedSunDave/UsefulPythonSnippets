# Useful Code Snippets - Controlling an Application w/ Pexpect

Controlling applications with python3 is a create mechanism for orchestration and automation. Pexpect is one such package that allows you control a variety of applications via automation.

Start by 'spawning' a child application, 'expect' a certain string of works that would normally appear in cli, and then 'sendline' the command that you want to execute. I found allowing a pause in between expect and sendline helps with making sure the program executes correctly.

[Pexpect Documentation](https://pexpect.readthedocs.io/en/stable/)

*Some of these solutions I found, and some of the I wrote myself. I will try my best to contain references to ones I found, in order to help keep track of where I found the solutions. As always, please feel free to reach out to me with any questions or concerns

## Collector

* **Dave Foran** - [RedSunDave](https://github.com/RedSunDave)
* **Red Sun Information Systems Website** - [Red Sun IS](https://redsunis.info)

## License

All of these scripts are free to use. I also do not claim to have written all of these codes just some of them. I have just found them to be useful, and they are available about the open source realms.

## Acknowledgments

* To all the people who contribute answers to help people to do code, thank you. Will do my best to document sources.
