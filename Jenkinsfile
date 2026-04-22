pipeline {

    agent { label 'my_slave' }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Samsonkunchala/pipeline_code.git'
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -ltr'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pipe_line_lab .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f pipe_line_lab || true
                docker run -d -p 8081:8081 --name pipe_line_lab pipe_line_lab
                '''
            }
        }

    }
}
