n < -100
beta <- 2
sx<-1
sy<- sx*2/0.8 
se<-sqrt(sy^2-2^2)
x<-rnorm(n)*sx
y= 2 * x + rnorm(n)*se
lm(y~x)
cor(y,x)^2
rnorm(x)
