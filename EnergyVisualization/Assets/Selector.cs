using UnityEngine;

public class Selector : MonoBehaviour
{
    private Camera cam;
    private IBuilding selection;

    private IBuilding Selection
    {
        set
        {
            selection.Deselect();
            selection = value;
            selection.Select();
        }
    }

    private void Awake()
    {
        cam = GetComponent<Camera>();
        selection = NullBuilding.Instance;
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
            Select();
    }

    private void Select()
    {
        RaycastHit hit;
        Ray ray = cam.ScreenPointToRay(Input.mousePosition);

        if (!Physics.Raycast(ray, out hit) || !hit.transform.TryGetComponent(out IBuilding building))
            return;

        if (building == selection)
            Selection = NullBuilding.Instance;
        else
            Selection = building;
    }
}
