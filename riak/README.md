# Riak

## Install

[Ubuntu/Debian](http://wiki.basho.com/Installing-on-Debian-and-Ubuntu.html)

    wget http://downloads.basho.com/riak/riak-1.1.1/riak_1.1.1-1_i386.deb
    sudo dpkg -i riak_1.1.1-1_i386.deb

Start/Stop/Restart your daemon:

    sudo /etc/init.d/riak start
    sudo /etc/init.d/riak stop
    sudo /etc/init.d/riak restart

Main config under `/etc/riak/app.config`.

## Drivers

* [nodejs](http://riakjs.org/)
* [erlang protobuf](https://github.com/basho/riak-erlang-client)

## Links

* [Riak](http://wiki.basho.com/)
* [Videos/Talks](http://vimeo.com/bashotech)
