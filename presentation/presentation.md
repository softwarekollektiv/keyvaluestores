# Key-Value-Stores

---

# Introduction

* Tokyo-Cabinet
* Riak
* Voldemort
* Scalaris

---

# Tokio Cabinet 

---

# Overview


---
# Architecture

---

# Data Model

---

# Replication


---

# Query-Language


# Cosistent Hasing

---

# Horizontal Scaling

---

# Eventual Cosistency

---

# Data models (types)

---

# Map/Reduce

---

# Riak

---

# Overview

* written in erlang
* developed by basho
* free software
* drivers in erlang, java, ruby, node

---
# Architecture
 * advanced distributed Key-Value-Store

---

# Data Model

* Buckets
* Keys
* Values

---

# Replication

* *n_val*
* *w*
* *r*

---

# Query-Language
* map/reduce
* secondary indexes


# Cosistent Hasing

---

# Horizontal Scaling

---

# Eventual Cosistency

---

# Data models (types)

---

# Map/Reduce

---

# Voldemort 
![Alt text](images/voldemort.png)

<!-- taken from Project Voldemort ppt from http://www.svforum.org/index.cfm?fuseaction=Document.filterdocumentlist&topicRadio=Topic&topicOnly=32&docPublishYear=getAllYears --!>

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
** json
** string
** java-serialization
** protobuf
** identity (bytes)
** write your own

---

#Basic Operations
*PUT
*GET
*GET_ALL
*DELETE

---

---
# Architecture
![Alt text](http://project-voldemort.com/images/logical_arch.png)
<!-- taken from http://project-voldemort.com/design.php --!>
---

#Eventual consistency
* Read-Repair
* Hinted Handoff 
** any-handoff (to any server)
** consisten-handoff (to server where replicas lie)
** proximity-handoff (to a server locally near)
.writes can be done to every node (in emergency) - periodically tries to update correct node


---

# Replication
* consistent hashing to store & retrieve data
** replicas configurable
* updates of outdated data by reads and writes
* versions controlled by Vector Clock

---

# Query-Language

---

