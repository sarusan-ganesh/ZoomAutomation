# Zoom Email Automation
A Python-based tool to automate the process of organizing Zoom recordings, renaming files for seamless categorization, and attaching them to emails with pre-defined recipients, subject lines, and body content.

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technologies Used and Prerequisites](#technologies-used-and-prerequisites)  
4. [Future Enhancements](#future-enhancements)  

## Project Overview 
The Zoom File Automation Tool streamlines post-meeting workflows by automating file transfers, renaming Zoom recordings for better organization, and sending them via email to the intended recipients. This eliminates the need for manual file handling and ensures consistent, timely sharing of meeting recordings and associated files.

## Features 
- **Automated File Transfer**: Moves downloaded Zoom files to a specified directory for organization.
- **Dynamic File Renaming**: Renames files based on predefined naming conventions (e.g., meeting date, topic, participants).
- **Email Integration**:
Attaches organized files to emails.
Automatically populates recipients, subject lines, and email bodies.
- **Error Logging**: Tracks and logs errors in file transfer or email delivery for troubleshooting.

## Technologies Used and Prerequisites
- **Programming Language**: Python
- **Libraries and APIs**:
  - os and shutil: For file handling and transfer.
  - datetime: For generating time-based file names.
  - smtplib and email: For email automation.
  - dotenv: For securely storing email credentials and configurations

- **Prerequisites**
  - Python 3.8+
  - Access to an email server (e.g., Gmail, Outlook).
  - Zoom files downloaded to a known directory

## Future Enhancements 
Add integration with cloud storage services (e.g., Google Drive, OneDrive) for file uploads.
Enhance user interface for configuring email and file settings.
Support multiple file formats and extended naming conventions.
Introduce email scheduling features for timed delivery
