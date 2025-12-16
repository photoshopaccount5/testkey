pipeline {
    agent any

    options {
        // Keeps the console clean and ensures GitHub sees the status
        buildDiscarder(logRotator(numToKeepStr: '10'))
        checkoutToSubdirectory('source')
    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins Multibranch automatically handles the checkout of the PR branch
                echo "Building Pull Request: ${env.CHANGE_ID}"
            }
        }

        stage('Python Syntax Check') {
            steps {
                script {
                    echo 'Checking Python syntax...'
                    sh 'python3 -m py_compile binarysearch.py'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    echo 'Running script...'
                    sh 'python3 binarysearch.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Build Passed! Updating GitHub status...'
            // This tells the GitHub PR that the "Gate" is cleared
        }
        failure {
            echo 'Build Failed! The PR will be blocked.'
        }
    }
}