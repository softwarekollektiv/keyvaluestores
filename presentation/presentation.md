# Key-Value-Stores

---

# Introduction

* Tokyo-Cabinet
* Voldemort
* Riak
* Scalaris
* Demo application

---

# Tokio Cabinet

---

# Overview


---

# Voldemort

![Alt text](images/voldemort.png)

<!-- taken from Project Voldemort ppt from http://www.svforum.org/index.cfm?fuseaction=Document.filterdocumentlist&topicRadio=Topic&topicOnly=32&docPublishYear=getAllYears -->

---

# Overview

* open-source reimplementation of Amazon Dynamo
* started by linkedIn
* latency is top priority
* now on github
* written in Java
* Clients in Java, Ruby, PHP, C++

---

# Data Model

* data in "stores"
* keys in stores unique
* one to many relations by lists
* serialization pluggable
    * json
    * string
    * java-serialization
    * protobuf
    * identity (bytes)
    * write your own

---

# Basic Operations

* PUT
* GET
* GET\_ALL
* DELETE

---

# Architecture

![Alt text](http://project-voldemort.com/images/logical_arch.png)

<!-- taken from http://project-voldemort.com/design.php -->

---

# Eventual consistency

* Read-Repair
* Hinted Handoff
    * any-handoff (to any server)
    * consisten-handoff (to server where replicas lie)
    * proximity-handoff (to a server locally near)
* writes can be done to every node (in emergency) - periodically tries to update correct node


---

# Replication

* consistent hashing to store & retrieve data
    * replicas configurable
* updates of outdated data by reads and writes
* versions controlled by Vector Clock

---

# Riak

---

# Overview

* written in erlang
* developed by Basho Technologies, Inc.
* Enterprise and open source version
* drivers in erlang, java, ruby, node

---

# Overview

* distributed (p2p)
* eventual consistent
* Replication
* ...

---

# Data Model

* Buckets
* Keys
* Values
* Meta-Data
* Links

---

# Basic Operations

* put, get, delete
* list buckets
* list keys

---

# Architecture

* Cluster: Set of physical hosts
* each hosts runs a Riak node
* each Riak node runs a set of virtual nodes (vnodes)

---

# The Ring

* diveded into partitions
    * number of partitions is configurable
    * "weighten" of hosts not possible (not implemented)
* vnodes "claim" a partition
* 160-bit binary hash of bucket/key pair
* every host in the cluster can function as coordinator
* gossip protocol to share ring state

---

# Backends

* Storage engines
    * leveldb, bitcask, in-memory, ...

---

# Eventual Consistent

* vector-clocks
* conflict resolution
    * last\_write\_wins (last write wins)
    * allow\_mult (return multiple versions)

---

# Replication

* Replication along the ring
* configurable per bucket
* handoff protocoll if nodes are unavailable
* "no guarantees that the three replicas will go to three separate physical nodes"
* *n_val*: number of copies stored in the cluster
* *w*: number of nodes that must return for successful read
* *r*: number of nodes that must return for successful write

---

# Query-Language

* Map/Reduce
    * Key-Filters
* Secondary Indexes

---

# Map/Reduce

* queries written in:
    * erlang
    * javascript
* executed on every node in the cluster

---

# Key-Filters

* map/reduce queries over keys
* can be used as input of a map/reduce job
* predicates like:
    * equal, greater than, member of set
* combine with logic operaters (and, or, not)

# Secondary Indexes
* Index on independent values
    * schema free
* indexable types: int, binary
* Local index per Partition
* You have to query all hosts in the cluster

---

# Scalaris

---

# Overview
