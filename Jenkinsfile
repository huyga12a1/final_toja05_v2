pipeline {
    
    agent none
    
    environment {
        
        DOCKERHUB_USERNAME = 'huyga12a1'
        DOCKERHUB_PWD = credentials('registry-pass')
        
        NODE_JS_REPO = 'https://github.com/huyga12a1/node-hello.git'
        NODE_JS_DIR = 'node-hello'
        
        PYTHON_REPO = 'https://github.com/huyga12a1/python-hello.git'
        PYTHON_APP = 'python-hello'
    }

    parameters { 
      choice(name: 'CHOICES', 
             choices: ['nodejs', 'python', 'all'], 
             description: '',
             //required: true 
             ) 
    }
  
    stages {
        
        stage('Build NodeJs') {
            
            agent { label "master" }
            when {
                expression { 
                   return params.CHOICES == 'nodejs'
                }
            }
           steps {
               sh './nodejs/build.sh'
            }
        }
        
        
        stage('Build Python') {
            
            agent { label "master" }
            when {
                expression { 
                   return params.CHOICES == 'python'
                }
            }
           steps {
                sh './python/build.sh'
            }
        }
        
        
        stage('Build All') {
            
            when { 
                expression { 
                   return params.CHOICES == 'all'
                }
            }
           parallel {
               
                stage('Build NodeJs') {
                    agent { label "master" }
                    steps {
                        sh './nodejs/build.sh'
                    }
                }
                stage('Build Python') {
                    agent { label "master" }
                    steps {
                        sh './python/build.sh'
                    }
                }
            }
        }
        
        
        stage('Push NodeJs') {
            
            agent { label "master" }
            when { 
                expression { 
                   return params.CHOICES == 'nodejs'
                }
            }
           steps {
               sh './nodejs/push.sh'
            }
        }
        
        stage('Push Python') {
            
            agent { label "master" }
            when { 
                expression { 
                   return params.CHOICES == 'python'
                }
            }
           steps {
                 sh './python/push.sh'
            }
        }
        
        stage('Push All') {
            
            when { 
                expression { 
                   return params.CHOICES == 'all'
                }
            }
            parallel {
               
                stage('Push NodeJs') {
                    agent { label "master" }
                    steps {
                        sh './nodejs/push.sh'
                    }
                }
                stage('Push Python') {
                    agent { label "master" }
                    steps {
                        sh './python/push.sh'
                    }
                }
            }
        }
        
        
        stage('Deploy NodeJs') {
            
            agent { label "centos-03" }
            when { 
                expression { 
                   return params.CHOICES == 'nodejs'
                }
            }
           steps {
                sh './nodejs/deploy.sh'
            }
        }
        
        
        stage('Deploy Python') {
            
            agent { label "centos-03" }
            when { 
                expression { 
                   return params.CHOICES == 'python'
                }
            }
           steps {
                 sh './python/deploy.sh'
            }
        }
        
        
        stage('Deploy All') {
            
           
            when { 
                expression { 
                   return params.CHOICES == 'all'
                }
            }
            parallel {
               
                stage('Deploy NodeJs') {
                    agent { label "centos-03" }
                    steps {
                        sh './nodejs/deploy.sh'
                    }
                }
                stage('Deploy Python') {
                    agent { label "centos-03" }
                    steps {
                        sh './python/deploy.sh'
                    }
                }
            }
        }

    }
}
