hosts: all
  become: yes
  tasks:
  - name: Install packages
    apt:
      name:
      - vim
      - zip
      state: latest