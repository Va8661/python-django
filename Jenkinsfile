pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Va8661/python-django.git'
            }
        }
        stage('Build and Deploy') {
            steps {
                sh 'pip install django'
                sh 'cd webapp'
                sh 'python3 manage.py migrate'
                sh 'python3 manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
