resort.data <- read.csv('../Data/resort_data.csv', header=TRUE)

require('ggplot2')

resort.data$log_skiable_area = log(resort.data$skiable_area)
resort.data$log_trails = log(resort.data$trails)


ggplot(resort.data, aes(x=log_skiable_area, y=log_trails)) +
  geom_point(shape=16,alpha=1/4, color="#FF7400", size = 3) + 
  #geom_text(aes(label=name),hjust=1, vjust=0, color='#999999') +
  theme(panel.grid.minor=element_blank(), panel.grid.major=element_blank(), 
        panel.background = element_blank(), 
        plot.background = element_rect(fill='#1C1C1C'),
        text=element_text(color='#999999'),
        title = element_text(lineheight=.2, size=16),
        axis.title.x = element_text(vjust=-.1),
        axis.ticks=element_blank(),
        axis.text=element_blank(),
        axis.title.y = element_text(vjust=.3)) +
  xlab('Skiable Acres') +
  ylab('Number of Trails') +
  ggtitle('Skiable Acres vs. Trails') + 
  geom_smooth(method=lm,   # Add linear regression lines
              se=FALSE,    # Don't add shaded confidence region
              fullrange=T, # Extend regression lines
              color = '#1240AB' ) 
# export 15 x 10
  
  