# Riak

## Install

### Production

[Ubuntu/Debian](http://wiki.basho.com/Installing-on-Debian-and-Ubuntu.html)

    wget http://downloads.basho.com/riak/riak-1.1.1/riak_1.1.1-1_i386.deb
    sudo dpkg -i riak_1.1.1-1_i386.deb

Start/Stop/Restart your daemon:

    sudo /etc/init.d/riak start
    sudo /etc/init.d/riak stop
    sudo /etc/init.d/riak restart

Main config under `/etc/riak/app.config`.

### Development

[Setup a dev environment](http://wiki.basho.com/Building-a-Development-Environment.html)

    cd bin
    wget http://downloads.basho.com/riak/CURRENT/riak-1.1.1.tar.gz
    tar -xvf riak-1.1.1.tar.gz
    cd riak-1.1.1
    make all
    make devrel
    cd dev

Start cluster nodes:

    dev1/bin/riak start
    dev2/bin/riak start
    dev3/bin/riak start

Build the cluster:

    dev2/bin/riak-admin join dev1@127.0.0.1
    dev3/bin/riak-admin join dev1@127.0.0.1

Check the member status:

    ./dev1/bin/riak-admin member_status

## Drivers

* [nodejs](http://riakjs.org/)
* [erlang protobuf](https://github.com/basho/riak-erlang-client)
* [python](https://github.com/basho/riak-python-client)

## Backends

## Links

* [Riak](http://wiki.basho.com/)
* [Videos/Talks](http://vimeo.com/bashotech)

## Concepts

* buckets
* [links](http://wiki.basho.com/Links.html)
* [map/reduce](http://wiki.basho.com/MapReduce.html)
* [search](http://wiki.basho.com/Riak-Search.html)
* [key filters](http://wiki.basho.com/Key-Filters.html)
