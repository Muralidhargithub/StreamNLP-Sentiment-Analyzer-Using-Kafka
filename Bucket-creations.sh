# Create raws3bucket
aws s3api create-bucket --bucket raws3bucket --region your-preferred-region --create-bucket-configuration LocationConstraint=your-preferred-region

# Create results3bucket
aws s3api create-bucket --bucket results3bucket --region your-preferred-region --create-bucket-configuration LocationConstraint=your-preferred-region
