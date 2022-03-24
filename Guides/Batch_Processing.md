#### What Is a Batch?
[Taken from Machine Learning Mastery](https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/)

🌟The batch size is a hyperparameter that defines the number of samples to work through before updating the internal model parameters.🌟

Think of a batch as a for-loop iterating over one or more samples and making predictions. At the end of the batch, the predictions are compared to the expected output variables and an error is calculated. From this error, the update algorithm is used to improve the model, e.g. move down along the error gradient.

A training dataset can be divided into one or more batches.

When all training samples are used to create one batch, the learning algorithm is called batch gradient descent. When the batch is the size of one sample, the learning algorithm is called stochastic gradient descent. When the batch size is more than one sample and less than the size of the training dataset, the learning algorithm is called mini-batch gradient descent.

|Type | Description|
| :---: | :---: | 
|Batch Gradient Descent | Batch Size = Size of Training Set|
|Stochastic Gradient Descent| Batch Size = 1|
|Mini-Batch Gradient Descent| 1 < Batch Size < Size of Training Set|


Back-propagation has three main variations: batch, online and mini-batch. 

#### For Example :-

Assume you have a dataset with 200 samples (rows of data) and you choose a batch size of 5 and 1,000 epochs.<br>
This means that the dataset will be divided into 40 batches, each with five samples. The model weights will be updated after each batch of five samples.
This also means that one epoch will involve 40 batches or 40 updates to the model.

With 1,000 epochs, the model will be exposed to or pass through the whole dataset 1,000 times. That is a total of 40,000 batches during the entire training process.




#### 🎇Matheamtics :- 

[Taken from StackExchange](https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network/)

Consider Gradient Descent as an optimization algorithm to minimize your Loss function J(θ). The updating step in Gradient Descent is given by
![image](https://user-images.githubusercontent.com/51333577/159855920-c4052cba-83ee-4ddb-9913-1ea0c5cdc2bb.png)


Stochastic Gradient Descent <br>![Stochastic Gradient Descent](https://user-images.githubusercontent.com/51333577/159855656-bd21e512-a716-44aa-af85-dc288d3a6fa2.png)

Full-Batch Gradient Descent <br>![image](https://user-images.githubusercontent.com/51333577/159856308-dde02cd2-4e65-40d6-99cb-e1573d8cb5ea.png)


#### 📃 Simple algorithms and comparison :-

[Taken from Visual Studio Magazine](https://visualstudiomagazine.com/articles/2017/10/01/batch-training.aspx)

Batch and online training differ slightly in how the weight gradients are calculated and when the weights are updated. In pseudo-code, online back-propagation training for a single training epoch is:

```
loop each training item
  compute output values
  for-each weight
    use target and output to compute gradient
  end-for
  for-each weight
    use gradient to compute weight delta
    use delta to update weight
  end-for
end-loop
```

Notice that in online training, each weight is updated based on the computed output results of a single training item. In pseudo-code, batch online training for a single training epoch is:

```
loop each training item
  compute output values
  for-each weight
    use target and output to compute gradient
    accumulate gradient value
  end-for
end-loop
for-each weight
  use accumulated gradient to compute delta
  use delta to update weight
end-for
```

The key difference in batch training is that each weight update is based on an accumulated gradient that in turn is based on the results of all training items. Put another way, batch training updates a weight based on all available gradient information, but online training uses a single training item to essentially estimate the total gradient.
