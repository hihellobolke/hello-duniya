#!/bin/bash

config_text="port 2222"

if [[ "$(grep -c "${config_text}" /etc/ssh/sshd_config)" -gt 0 ]]; then
    echo "already added"
else 
    echo "${config_text}" >> /etc/ssh/sshd_config
fi