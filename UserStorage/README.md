# User Storage App

An application for storing, saving, loading, and dispalying user data. 

#### Contents
- [User Storage App](#user-storage-app)
      - [Contents](#contents)
  - [1. Introduction](#1-introduction)
  - [2. Challenges](#2-challenges)
  - [3. API Overview](#3-api-overview)
  - [4. Dependencies](#4-dependencies)

## 1. Introduction

The `UserStorage` app is comprised of two primary components: the `UserStorage` and `App` classes. The `UserStorage` class is an object with an integrated API which handles the creation, addition, serialisation, and formatting of user data. The `App` class, on the other hand, is a CLI application which provides a user-friendly interface to `UserStorage`. 

## 2. Challenges

The main challenges that were anticipated when creating this API are summarised below:

* <b>Finding the correct packages:</b> Python has a myriad of different modules which can be used to automate certain processes. Finding the right one is a time consuming and somewhat overwhelming process at times. This was overcome by sticking to a simple rule: where possible, use official Python packages. 
* <b>Working out what should be custom made, and what should be imported:</b> Since Python does have such a large variety of content, it's often hard to know what you need to write, and what you can just import. The decision was eventually made to custom build all modules that require application-specific logic. For example, the actual `UserStorage` object would need my own custom logic, but a `YAML` parser, which is complex beyond the scope of the project, would be imported. 
* <b>Separating code into Modules:</b> Separating responsibilities between every module would prove to be an interesting problem to solve. In theory, the `UserStorage` object could handle all logic, but this would make the class incredibly large and complex. 
     * A decision was eventually made to separate the modules into four primary modules: `UserStorage`, `App`, `Utils`, `Serialisation` and `Formatting`. Each of these would handle their specific tasks and would be combined within the CLI application.

## 3. API Overview




## 4. Dependencies