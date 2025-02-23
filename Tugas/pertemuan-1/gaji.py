__r   r   c              	   C   sä   t |dkr|S |jD ]d}| j}|st t |¡}|s)tdt | d |  S |D ]C\}}||d  }||d  }t |d¡}	t |d¡}
|	sK|
rLq+tj	|t
|d t
|d ft
|d t
|d f| j ¡ | jd q+q|S )a  
        Annotates the given scene by drawing lines between specified key points to form
        edges.

        Args:
            scene (ImageType): The image where skeleton edges will be drawn. `ImageType`
                is a flexible type, accepting either `numpy.ndarray` or
                `PIL.Image.Image`.
            key_points (KeyPoints): A collection of key points where each key point
                consists of x and y coordinates.

        Returns:
            Returns:
                The annotated image, matching the type of `scene` (`numpy.ndarray`
                    or `PIL.Image.Image`)

        Example:
            ```python
            import supervision as sv

            image = ...
    