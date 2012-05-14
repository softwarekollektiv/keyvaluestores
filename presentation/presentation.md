# Key-Value-Stores

---

# Introduction

* Tokyo-Cabinet
* Riak
* Voldemort
* Scalaris

---

# Riak

---

# Overview

* written in erlang
* developed by basho
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
* queries written in erlang or javascript
* executed on all cluster nodes

# Key-Filters
* map/reduce queries over keys
* can be used as input of a map/reduce job
* predicates like
    * equal, greater than, member of set
* logic operaters (and, or, not)

# Secondary Indexes
* Index on independent values
    * schema free
* indexable types: int, binary
* Local index per Partition
* Query all hosts in the cluster

---

# Scalaris

---

# Overview

---
